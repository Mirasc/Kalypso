
import os ,sys
import json
import requests

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
		self.preview_img_path = ''
		self.smms_json = {}
		self.smms_headers = ''
		self.history_json = {'history':[]}
		self.history = []

		self.kalypso.openFilePushButton.clicked.connect(self.open_file)
		self.kalypso.uploadPushButton.clicked.connect(self.upload_file)
		self.kalypso.cancelPushButton.clicked.connect(self.cancel_upload)
		self.kalypso.uploadedListWidget.itemClicked.connect(self.uploaded_item_clicked)
		self.kalypso.uploadedListWidget.itemDoubleClicked.connect(self.uploaded_item_double_clicked)
		# self.kalypso.closeEvent()

		self.kalypso.actionSet_AuthCode.triggered.connect(self.set_authcode)

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
		with open('SMMS_JSON.json', 'r') as smms_json_file:
			self.smms_json = json.load(smms_json_file)
		self.smms_headers = self.smms_json['Headers']
		if self.smms_headers == '':
			reply = QMessageBox.information(self.kalypso, 'information', 'Please input your Authorization code!', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
			if reply==QMessageBox.Yes:
				self.authcode.show()
			else:
				QMessageBox.information(self.authcode, 'information', 'Your Uploadings Will Be Only Kept Locally!', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

	def show_preview_img(self):
		self.graphicsView_width = self.kalypso.graphicsView.width()
		self.preview_img_pixmap = QPixmap(self.preview_img_path)
		self.preview_img_width = self.preview_img_pixmap.width()
		self.preview_img_zoomscale = self.graphicsView_width / self.preview_img_width - 0.05
		self.img_item = QGraphicsPixmapItem(self.preview_img_pixmap)
		self.img_item.setScale(self.preview_img_zoomscale)
		self.img_scene = QGraphicsScene()
		self.img_scene.addItem(self.img_item)
		self.kalypso.graphicsView.setScene(self.img_scene)

	def open_file(self):
		self.tobe_uploaded_path, _ = QFileDialog.getOpenFileName(self.kalypso, directory=os.getcwd())
		self.preview_img_path = self.tobe_uploaded_path
		self.show_preview_img()

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
		self.file_path = ''

	def set_authcode(self):
		self.authcode.show()

	def authcode_ok(self):
		code = self.authcode.authCodeLineEdit.text()
		if not len(code) == 32:
			QMessageBox.information(self.kalypso, 'warning', 'Authorization code error!', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
		else:
			self.smms_headers = {"Authorization": code}
			self.smms_json['Heasers'] = self.smms_headers
			with open('SMMS_JSON.json' ,'w') as smms_json_file:
				json.dump(self.smms_json, smms_json_file, indent=4, ensure_ascii=False)
			self.authcode.hide()

	def authcode_cancel(self):
		self.authcode.hide()

	def save_history(self):
		self.history_json['history'] = self.history
		with open('history.json' ,'w') as history_json_file:
			json.dump(self.history_json, history_json_file, indent=4, ensure_ascii=False)

	def uploaded_item_clicked(self):
		# 下载 item 对应的图片 保存 并返回保存路径
		# self.preview_img_path =
		self.show_preview_img()

	def uploaded_item_double_clicked(self):
		# 复制item的链接到剪贴板
		pass

if __name__ == '__main__':
	app = QApplication(sys.argv)
	mainapp = main()
	mainapp.kalypso.show()
	sys.exit(app.exec_())
