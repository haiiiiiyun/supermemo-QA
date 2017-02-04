#!/usr/bin/python -u
# -*- coding: utf-8 -*-

# original: https://github.com/eyedol/tools/blob/master/anki_data_builder.py

import sqlite3
import sys
import argparse

__version__ = '1.0.0'

class CardBuilder:
  def __init__(self, sqlite_input_file):
    self.sqlite_input = sqlite_input_file

  def dump_qa(self,):
    conn = sqlite3.connect(self.sqlite_input)
    conn.text_factory = str ## my current (failed) attempt to resolve this
    cursor = conn.cursor()
    data = cursor.execute("SELECT type, front, back FROM cards")
    self.__output_qa(data);

  def __output_qa(self, items):
      # type 1: general
      #      2: code
      for index, item in enumerate(items):
          if index != 0:
              print ''

          #if item[0] == 2:
          q = item[1].replace("\r\n", "<br/>")
          q = q.replace("\r", "<br/>")
          q = q.replace("\n", "<br/>")
          a = item[2].replace("\r\n", "<br/>")
          a = a.replace("\r", "<br/>")
          a = a.replace("\n", "<br/>")
          d = ["Q:", q, '\n', "A:", a]
          print ''.join(d)


if __name__ == '__main__':
  """
    Sample usage: ./jwasham_data_builder.py ~/cards-jwasham-extreme.db > /CS-QA.txt
  """
  parser = argparse.ArgumentParser(description='Exports Flash cards sqlite3 data to QA for supermemo import.')
  parser.add_argument('sqlite_file', help="Full path to the flash cards sqlite3 db file. Include file name.")
  args = parser.parse_args()

  sqlite_file = args.sqlite_file
  qa = CardBuilder(sqlite_file)
  qa.dump_qa()
