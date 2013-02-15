# spec/model/usermodel_spec.rb
require 'spec_helper'
# require_relative '../../models/user'

describe User do

  after(:each) do
  	User.delete_all
  end

  it "creates a valid user" do
    User.create(:user => "username", :password => "password", :count => 1).should be_valid
  end

  it "finds a valid user" do
  	User.create(:user => "username", :password => "password", :count => 1)
  	User.find_by_user("username").should be_valid
  end

  it "does not find invalid user" do
  	User.create(:user => "username", :password => "password", :count => 1)
  	User.find_by_user("sunshine").should be_nil
  end

  describe "adding a user" do
	it "errorCode should not be -1" do
		response = User.add("noob","l33t")
		response[:errCode].should_not eql(-1)
	end
  end	

  describe "adding with empty username" do
	it "errorCode should be -3" do
		response = User.add("","noob")
		response[:errCode].should eql(-3)
	end
  end

  describe "user count" do
	it "errorCode should be 1" do
		response = User.add("noob","nubcake")
		response[:count].should eql(1)
	end
  end

  describe "long username fails" do
	it "errorCode should be -3" do 
		response = User.add('u'*129,"noob")
		response[:errCode].should eql(-3)
	end
  end

  describe "long password fails" do
	it "errorCode should be -4" do 
		response = User.add('noob',"u"*129)
		response[:errCode].should eql(-4)
	end
  end

  describe "correct login" do
    it "errorCode should be 1" do 
		User.add('nub',"noob")
		response = User.login('nub',"noob")
		response[:errCode].should eql(1)
	end
  end

  describe "login increases count by 1" do
	it "response should be 2" do 
		User.add('bo',"asdfasdf")
		User.login('bo',"asdfasdf")
		response = User.find_by_user('bo').count
		response.should eql(2)
	end
  end
  
end