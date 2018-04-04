import cmd
import csv
import urllib.request
import ssl
import json

class AmazonShell(cmd.Cmd):
    intro = "\nWelcome to the Amazon Shell (ash).\nType `help` or `?` to list commands.\n"
    prompt = '> '
    event = None

    def do_q(self, arg):
      """Quit"""
      return True

    def do_EOF(self, arg):
      return True

    def do_catalog(self, arg):
      """Browse Amazon's product catalog"""
      for product in self.read_catalog():
        print("ASIN :", product["ASIN"])
        print("Price:", "$" + str(product["price"]))

        print(product["title"])
        print()
        print(product["description"])
        print("-"*70)
        print()

    def read_catalog(self):
      url = "https://www.jeffcohenonline.com/amazon.json"
      ctx = ssl.create_default_context()
      ctx.check_hostname = False
      ctx.verify_mode = ssl.CERT_NONE
      data = urllib.request.urlopen(url, context=ctx).read().decode('utf8')
      return json.loads(data)


if __name__ == '__main__':
    AmazonShell().cmdloop()












      # rows = []
      # with open('amazon.csv') as csv_file:
      #   catalog = csv.DictReader(csv_file)
      #   for row in catalog:
      #     rows.append(row)
      # return rows
