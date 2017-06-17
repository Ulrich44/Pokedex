import tornado.web
import base64
from tornado.ioloop import IOLoop

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hola, mundo")

class PokemonHandler(tornado.web.RequestHandler):
    def post(self):

       try:
           pokemon_name = self.get_argument("pokemon")
           img_base64 = self.get_argument("photo")

           with open("{}.jpg".format(pokemon_name),"wb") as file_writer:
            file_writer.write(base64.b64decode(img_base64))


           self.write("true")
       except Exception as ex:
           print(ex)
           self.write("false")

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/?", MainHandler)
        ]

        tornado.web.Application.__init__(self, handlers)

def main():
    app = Application()
    app.listen(80)
    IOLoop.instance().start()

if __name__ == "__main__":
    main()