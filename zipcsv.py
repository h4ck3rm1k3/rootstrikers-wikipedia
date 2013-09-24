import zipfile
import os


class ZipCSV:
    # def process_csv (self, filename):
    #     zfile = zipfile.ZipFile(filename)
    #     for name in zfile.namelist():
    #         (dirname, filename) = os.path.split(name)
    #         print "reading " + filename + " on " + dirname
    #         d = zfile.read(name)
    #         for l in d.split("\n"):
    #             self.process(l)

    def process_generate (self, filename, classname, parser, out):
        zfile = zipfile.ZipFile(filename)
        for name in zfile.namelist():
            (dirname, filename) = os.path.split(name)
            #print "reading " + filename + " on " + dirname
            d = zfile.read(name)
            out_file = out.create_file(name)
            parser.parse_file_data(filename, dirname, d, out_file)
            out_file.close()
