"""
Each file that starts with test... in this directory is scanned for subclasses of unittest.TestCase or testLib.RestTestCase
"""
import unittest
import os
import testLib

class TestAddUser2(testLib.RestTestCase):
    """Test adding users"""
    def assertResponse(self, respData, count = None, errCode = testLib.RestTestCase.ERR_BAD_USERNAME):
        """
        Check that the response data dictionary matches the expected values
        """
        expected = { 'errCode' : errCode }
        if count is not None:
            expected['count']  = count
        self.assertDictEqual(expected, respData)

    def testAdd(self):
        respData = self.makeRequest("/users/add", method="POST", data = { } )
        self.assertResponse(respData, count = None)

class TestAddUser3(testLib.RestTestCase):
    """Test adding users"""
    def assertResponse(self, respData, count = None, errCode = testLib.RestTestCase.ERR_BAD_PASSWORD):
        """
        Check that the response data dictionary matches the expected values
        """
        expected = { 'errCode' : errCode }
        if count is not None:
            expected['count']  = count
        self.assertDictEqual(expected, respData)

    def testAdd(self):
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'user1', 'password' : 'passwordasdfdasfsadfsadfsdfdsfsdfsdfasdfsadfasdfsadfsadfasdfasdfasdfasfasdfasdfdsafasdfsdfsdfasdfasdfadsfasfasfasfasfasfsdfssdfadsfsafadsfsafsfsfsdsfsf'} )
        self.assertResponse(respData, count = None)
        
class TestAddUser4(testLib.RestTestCase):
    """Test adding users"""
    def assertResponse(self, respData, count = None, errCode = testLib.RestTestCase.ERR_USER_EXISTS):
        """
        Check that the response data dictionary matches the expected values
        """
        expected = { 'errCode' : errCode }
        if count is not None:
            expected['count']  = count
        self.assertDictEqual(expected, respData)

    def testAdd(self):
        self.makeRequest("/users/add", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
        self.assertResponse(respData, count = None)
        
class TestLoginUser1(testLib.RestTestCase):
    """Test adding users"""
    def assertResponse(self, respData, count = 2, errCode = testLib.RestTestCase.SUCCESS):
        """
        Check that the response data dictionary matches the expected values
        """
        expected = { 'errCode' : errCode }
        if count is not None:
            expected['count']  = count
        self.assertDictEqual(expected, respData)

    def testLogin(self):
        self.makeRequest("/users/add", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
        respData = self.makeRequest("/users/login", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
        self.assertResponse(respData, count = 2)
        
class TestLoginUser2(testLib.RestTestCase):
    """Test adding users"""
    def assertResponse(self, respData, count = None, errCode = testLib.RestTestCase.ERR_BAD_CREDENTIALS):
        """
        Check that the response data dictionary matches the expected values
        """
        expected = { 'errCode' : errCode }
        if count is not None:
            expected['count']  = count
        self.assertDictEqual(expected, respData)

    def testLogin(self):
        self.makeRequest("/users/add", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
        respData = self.makeRequest("/users/login", method="POST", data = { 'user' : '', 'password' : 'password'} )
        self.assertResponse(respData, count = None)
        
class TestLoginUser3(testLib.RestTestCase):
    """Test adding users"""
    def assertResponse(self, respData, count = None, errCode = testLib.RestTestCase.ERR_BAD_CREDENTIALS):
        """
        Check that the response data dictionary matches the expected values
        """
        expected = { 'errCode' : errCode }
        if count is not None:
            expected['count']  = count
        self.assertDictEqual(expected, respData)

    def testLogin(self):
        self.makeRequest("/users/add", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
        respData = self.makeRequest("/users/login", method="POST", data = { 'user' : 'user1', 'password' : 'pass'} )
        self.assertResponse(respData, count = None)
        
class TestLoginUser4(testLib.RestTestCase):
    """Test adding users"""
    def assertResponse(self, respData, count = 3, errCode = testLib.RestTestCase.SUCCESS):
        """
        Check that the response data dictionary matches the expected values
        """
        expected = { 'errCode' : errCode }
        if count is not None:
            expected['count']  = count
        self.assertDictEqual(expected, respData)
        
    def testLogin(self):
        self.makeRequest("/users/add", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
        self.makeRequest("/users/login", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
        respData = self.makeRequest("/users/login", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
        self.assertResponse(respData, count = 3)
    
