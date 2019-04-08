from  testcase.testjiupai import Jiupai
from  util import BSTestRunner
import os,unittest,time


if __name__=='__main__':
    suite = unittest.TestSuite()
    now =time.strftime('%Y-%m%d',time.localtime(time.time()))
    basedir = os.path.abspath(os.path.dirname(__file__))
    file_dir = os.path.join(basedir,'testresult')
    file = os.path.join(file_dir,(now+'.html'))

    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Jiupai))
    re_open = open(file,'wb')
    runner =BSTestRunner.BSTestRunner(stream = re_open,title='demo of jiupai',description='test result0408')
    runner.run(suite)
