from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
  return "<p>Nama : Reza Ata Fadhillah</p><p>Tempat, Tanggal Lahir : Jakarta, 23 Mei 2004</p><p>Agama : Islam</p><p>Alamat : Jl. Bukit Tanggul</p><p>Jenis Kelamin : Laki-laki
</p><p>Umur : 19 tahun</p>"

        
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
