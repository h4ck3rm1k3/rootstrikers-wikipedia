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

    def process_generate (self, baseurl, urlfile, filename, classname, parser, out):
        zfile = zipfile.ZipFile(filename)
        for name in zfile.namelist():
            (dirname, ifilename) = os.path.split(name)
#            print "reading  filename %s from source %s" %  (ifilename, filename)
            d = zfile.read(name)
            out_file = out.create_file(ifilename, filename, baseurl, urlfile)
            parser.parse_file_data(ifilename, filename, d, out_file)
            out_file.close()
