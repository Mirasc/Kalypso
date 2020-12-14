import os, sys
import json
import shutil

import requests
import pathlib

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from mainui import Kalypso
from authcodeui import AuthCode


class main():
	def __init__(self):
		self.kalypso = Kalypso()
		self.authcode = AuthCode()

		self.tobe_uploaded_path = ''
		self.preview_img_index = 0
		self.preview_img_path = ''
		self.smms_json = {}
		self.smms_headers = ''
		self.history_json = {'history': []}
		self.history = []

		self.kalypso.openFilePushButton.clicked.connect(self.open_file)
		self.kalypso.uploadPushButton.clicked.connect(self.upload_file)
		self.kalypso.cancelPushButton.clicked.connect(self.cancel_upload)
		self.kalypso.copyUrlPushButton.clicked.connect(self.copy_img_url)
		self.kalypso.copyPagePushButton.clicked.connect(self.copy_img_page)
		self.kalypso.deletePushButton.clicked.connect(self.delete_img)
		self.kalypso.uploadedListWidget.itemClicked.connect(self.uploaded_item_clicked)
		self.kalypso.uploadedListWidget.itemDoubleClicked.connect(self.uploaded_item_double_clicked)
		# self.kalypso.closeEvent()

		self.kalypso.actionUpload.triggered.connect(self.open_file)
		self.kalypso.actionSet_AuthCode.triggered.connect(self.set_authcode)
		self.kalypso.actionClear_Cache.triggered.connect(self.clear_cache)

		self.authcode.okPushButton.clicked.connect(self.authcode_ok)
		self.authcode.cancelPushButton.clicked.connect(self.authcode_cancel)

		self.load_history()
		self.check_json()

	def load_history(self):
		try:
			with open('history.json', 'r') as history_json_file:
				self.history_json = json.load(history_json_file)
			self.history = self.history_json['history']
			for item in self.history:
				self.kalypso.uploadedListWidget.addItem(item['data']['filename'])
		except:
			pass

	def check_json(self):
		try:
			with open('SMMS_JSON.json', 'r') as smms_json_file:
				self.smms_json = json.load(smms_json_file)
			self.smms_headers = self.smms_json['Headers']
			if self.smms_headers == '':
				reply = QMessageBox.information(self.kalypso, 'information', 'Please input your Authorization code!', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
				if reply == QMessageBox.Yes:
					self.authcode.show()
				else:
					QMessageBox.information(self.authcode, 'information', 'Your Uploadings Will Be Only Kept Locally!', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
		except:
			reply = QMessageBox.warning(self.authcode, 'warning', 'SMMS_JSON.json file not exists,Please input your Authorization code!', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
			if reply == QMessageBox.Yes:
				self.smms_json = {
					"Version": "13.0.1",
					"Name": "sm.ms",
					"DestinationType": "ImageUploader",
					"RequestMethod": "POST",
					"RequestURL": "https://sm.ms/api/v2/upload",
					"Headers": {
						"Authorization": ""
					},
					"Body": "MultipartFormData",
					"Arguments": {
						"format": "json"
					},
					"FileFormName": "smfile",
					"URL": "$json:data.url$"
				}
				self.authcode.show()
			else:
				QMessageBox.information(self.authcode, 'information', 'Your Uploadings Will Be Only Kept Locally!', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

	def show_preview_img(self):
		preview_img_name = self.preview_img_path.split('/')[-1]
		self.kalypso.previewLabel.setText(preview_img_name)
		self.graphicsView_width = self.kalypso.graphicsView.width()
		self.graphicsView_height = self.kalypso.graphicsView.height()
		self.preview_img_pixmap = QPixmap(self.preview_img_path)
		self.preview_img_width = self.preview_img_pixmap.width()
		self.preview_img_height = self.preview_img_pixmap.height()
		self.preview_img_zoomscale_w = self.graphicsView_width / self.preview_img_width - 0.05
		self.preview_img_zoomscale_h = self.graphicsView_height / self.preview_img_height - 0.05
		self.preview_img_zoomscale = min(self.preview_img_zoomscale_w, self.preview_img_zoomscale_h)
		self.img_item = QGraphicsPixmapItem(self.preview_img_pixmap)
		self.img_item.setScale(self.preview_img_zoomscale)
		self.img_scene = QGraphicsScene()
		self.img_scene.addItem(self.img_item)
		self.kalypso.graphicsView.setScene(self.img_scene)

	def open_file(self):
		self.tobe_uploaded_path, _ = QFileDialog.getOpenFileName(self.kalypso, directory=os.getcwd())
		self.preview_img_path = self.tobe_uploaded_path
		self.show_preview_img()

	def clear_cache(self):
		del_list = os.listdir('./temp/')
		for f in del_list:
			file_path = os.path.join('./temp/', f)
			if os.path.isfile(file_path):
				os.remove(file_path)
			elif os.path.isdir(file_path):
				shutil.rmtree(file_path)

	def upload_file(self):
		files = {'smfile': open(self.tobe_uploaded_path, 'rb')}
		result = requests.post('https://sm.ms/api/v2/upload', files=files, headers=self.smms_headers).json()
		if result['code'] == 'success':
			self.history.append(result)
			self.kalypso.uploadedListWidget.addItem(result['data']['filename'])

			self.save_history()
			QMessageBox.information(self.kalypso, 'information', 'Upload Succcess!', QMessageBox.Yes, QMessageBox.Yes)
		elif result['code'] == 'image_repeated':
			QMessageBox.information(self.kalypso, 'warning', result['message'], QMessageBox.Yes, QMessageBox.Yes)
		else:
			QMessageBox.information(self.kalypso, 'warning', 'Upload Failed,Please Try Again!', QMessageBox.Yes, QMessageBox.Yes)

	def cancel_upload(self):
		self.tobe_uploaded_path = ''

	def copy_img_url(self):
		clipboard = QApplication.clipboard()
		clipboard.setText(self.history[self.preview_img_index]['data']['url'])

	def copy_img_page(self):
		clipboard = QApplication.clipboard()
		clipboard.setText(self.history[self.preview_img_index]['data']['page'])

	def delete_img(self):
		try:
			response = requests.post(self.history[self.preview_img_index]['data']['delete'])
			if response.status_code == 200:
				self.history.remove(self.history[self.preview_img_index])
				self.save_history()
				QMessageBox.information(self.kalypso, 'information', 'Delete Successful', QMessageBox.Yes, QMessageBox.Yes)
			else:
				QMessageBox.information(self.kalypso, 'information', 'Delete Unsuccessful', QMessageBox.Yes, QMessageBox.Yes)
		except:
			QMessageBox.information(self.kalypso, 'information', 'Delete Unsuccessful', QMessageBox.Yes, QMessageBox.Yes)




	def set_authcode(self):
		self.authcode.show()

	def authcode_ok(self):
		code = self.authcode.authCodeLineEdit.text()
		if not len(code) == 32:
			QMessageBox.information(self.kalypso, 'warning', 'Authorization code error!', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
		else:
			self.smms_headers = {"Authorization": code}
			self.smms_json['Heasers'] = self.smms_headers
			with open('SMMS_JSON.json', 'w+') as smms_json_file:
				json.dump(self.smms_json, smms_json_file, indent=4, ensure_ascii=False)
			self.authcode.hide()

	def authcode_cancel(self):
		with open('SMMS_JSON.json', 'w+') as smms_json_file:
			json.dump(self.smms_json, smms_json_file, indent=4, ensure_ascii=False)
		self.authcode.hide()

	def save_history(self):
		self.history_json['history'] = self.history
		with open('history.json', 'w+') as history_json_file:
			json.dump(self.history_json, history_json_file, indent=4, ensure_ascii=False)

	def uploaded_item_clicked(self):
		# 点击预览
		# 下载 item 对应的图片 保存 并返回保存路径
		self.preview_img_index = self.kalypso.uploadedListWidget.currentRow()
		path_ele = self.history[self.preview_img_index]['data']['path'].split('/')
		self.preview_img_name = path_ele[-1]
		self.preview_img_dir = './temp/' + path_ele[1] + '/' + path_ele[2] + '/' + path_ele[3] + '/'
		self.preview_img_path = self.preview_img_dir + self.preview_img_name
		if not pathlib.Path(self.preview_img_dir).exists():
			os.makedirs(self.preview_img_dir)
		if not pathlib.Path(self.preview_img_path).exists():
			image = requests.get(self.history[self.preview_img_index]['data']['url'])
			if image.status_code == 200:
				with open(self.preview_img_path, 'wb+') as fp:
					fp.write(image.content)
			del image
		self.show_preview_img()

	def uploaded_item_double_clicked(self):
		# 双击复制引用链接
		self.preview_img_index = self.kalypso.uploadedListWidget.currentRow()
		clipboard = QApplication.clipboard()
		clipboard.setText(self.history[self.preview_img_index]['data']['url'])


if __name__ == '__main__':
	app = QApplication(sys.argv)
	mainapp = main()
	mainapp.kalypso.show()
	sys.exit(app.exec_())
