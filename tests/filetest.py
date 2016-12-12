import unittest
from pisi.specfile import SpecFile
from pisi import uri
from pisi.file import File

class FileTestCase(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

    def testMakeUri(self):
        spec = SpecFile("repos/pardus-2007/system/base/curl/pspec.xml")
        url = uri.URI(spec.source.archive[0].uri)
<<<<<<< HEAD
        self.assertTrue(File.make_uri(url))

    def testChooseMethod(self):
        compress = File('repos/contrib-2007/pisi-index.xml', File.read)
        self.assertTrue(File.choose_method('pisi.conf', compress))
=======
        self.assert_(File.make_uri(url))

    def testChooseMethod(self):
        compress = File('repos/contrib-2007/pisi-index.xml', File.read)
        self.assert_(File.choose_method('pisi.conf', compress))
>>>>>>> littlebranch

    def testDecompress(self):
        localfile = File('repos/pardus-2007/system/base/curl/pspec.xml', File.read)
        compress = File('repos/contrib-2007/pisi-index.xml', File.read)
<<<<<<< HEAD
        self.assertTrue(File.decompress(localfile,compress))
=======
        self.assert_(File.decompress(localfile,compress))
>>>>>>> littlebranch

    def testLocalFile(self):
        f = File('repos/pardus-2007/system/base/curl/pspec.xml', File.read)
        r = f.readlines()
        assert (len(r) > 0)

    def testRemoteRead(self):
        f = File('http://www.gnu.org/licenses/gpl2.txt', File.read)
        r = f.readlines()
        assert (len(r) > 0)
