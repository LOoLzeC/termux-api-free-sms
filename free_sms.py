#!/usr/bin/env python2
# Made Full Of <3 By LOoLzeC
# Coded By: Deray
# Only Works In Indonesia

import re
import os
import json
import base64
import requests
import subprocess

# Color
W = '\033[1;37m' 
N = '\033[0m'
G = '\033[1;32m'
O = '\033[33m'
C = '\033[36m'
R = '\033[1;37m\033[31m'
B = '\033[1;37m\033[34m' 
notice  = "{}[*]{}".format(B,N)
warning = "{}[-]{}".format(R,N)
good    = "{}[!]{}".format(G,N)
warn    = "{}[!]{}".format(O,N)
ask = "{}[?]{}".format(R,N)

class sms(object):
	def __init__(self):
		os.system("clear")
		print("\t   [ Only Works In Termux Api ]")
		print("\t[ Made With Full Of <3 By LOoLzeC ]")
		print("\t       [ Coded By Deray ]\n")
		self.req=requests.Session()
		self.url=eval(
			base64.b64decode(
		"J2h0dHBzOi8vd3d3LnNtcy1ncmF0aXMueHl6L3t9Jw=="))
		self._scrap()
	
	# Ask
	def ask(self):
		r=raw_input("%s kirim lagi? y/n): "%(ask)).lower()
		if r =="y":
			sms()
	
	# Sending Metadata
	def send(self,url,**kwargs):
		self.req.post(url,data=kwargs)
		ok=self.req.post(self.url.format("cek.php"),
			data={
				"nomor":kwargs["nomor"],
				"pesan":kwargs["pesan"],
				"kirim2":"Kirim SMS"}).text
		if "SMS Berhasil Dikirim" in ok:
			print("%s Send Success."%(good))
			self.ask()
		else:
			print("%s failed bypass captcha."%(warning))
			self.ask()

	# Bypass Captcha Bot	
	def _scrap(self):
		hasil=[]
		bs=self.req.get(self.url.format("index.php")).text
		captcha=re.findall("\d \S \d",bs)[0]
		if "x" in captcha:
			hasil.append(
				int(captcha.split(" x ")[0])*int(captcha.split(" x ")[1]))
		if "+" in captcha:
			hasil.append(
				int(captcha.split(" + ")[0])+int(captcha.split(" + ")[1]))
		if "/" in captcha:
			hasil.append(
				int(captcha.split(" / ")[0])/int(captcha.split(" / ")[1]))
		if "-" in captcha:
			hasil.append(
				int(captcha.split(" - ")[0])-int(captcha.split(" - ")[1]))
		hasil.append(re.findall('hasil" value="(.*?)">',bs)[0])
		if len(hasil) ==2:
			self.nomer(hasil[0],hasil[1])
		else:
			exit("%s Gagal Bypass Captcha."%(warning))
	
	# Search Number
	def nomer(self,result,md5):
		target=[]
		self.q=raw_input("%s Nama Query Kontak: "%(
			ask)).lower()
		if self.q =="":
			return self.nomer(result,md5)
		else:
			print 
			for x in json.loads(
				subprocess.check_output(
					["termux-contact-list"])):
				if " " in x["number"] or "-" in x["number"]:
					continue
				else:
					if self.q in x["name"].lower():
						target.append(x["number"])
						print("%s. %s -> %s"%(len(target),
							x["name"].lower().replace(
								self.q,"%s%s%s"%(
									R,self.q,N)),x["number"]))
			if len(target) !=0:
				print 
				self.choice(result,md5,target)
			else:
				print(warning+" no result for: "+self.q)
				return self.nomer(result,md5)
		
	# Choice Number
	def choice(self,result,md5,target):
		try:
			self.num=input("%s Select: "%(ask))
		except Exception as __errors__:
			return self.choice(result,md5,target)
		self.message(result,md5,target[self.num-1])
	
	# Message Body And Sending Paramerer
	def message(self,result,md5,target):
		print("%s MAX: 100 characters"%(warn))
		self.msg=raw_input("%s Message: "%(ask))
		if self.msg =="":
			return self.msg(result,md5,target)
		else:
			self.send(
			self.url.format("verifikasi.php"),
				hasil=md5,
				nomor=target.replace("+62","0"),
				pesan=self.msg.replace("<s>","\n"),
				jawaban=result,
				kirim="Kirim SMS")

# Index Main
if __name__ == "__main__":
	sms()
