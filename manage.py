from app import create_app
from flask_script import Manager,Server
app=create_app('development')

manager=Manager(app)
manager.add_command('server',Server)

def test():
    """Run unit tests"""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
if __name__=="__main__":
    manager.run()
#Import create_app function from app folder and import Manger class from flask script
#Manager class will initialize our extension and server class that helps us launch our server
#We instantiate Manager class by passing in app instance
#Command line argument tells us how to run our application
#add_command()  creates a new command 'server' that launches our application server