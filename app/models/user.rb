# == Schema Information
#
# Table name: users
#
#  id         :integer          not null, primary key
#  user       :string(255)
#  password   :string(255)
#  count      :integer
#  created_at :datetime         not null
#  updated_at :datetime         not null
#

class User < ActiveRecord::Base
  attr_accessible :password, :user, :count

  SUCCESS = 1
  ERR_BAD_CREDENTIALS = -1
  ERR_USER_EXISTS = -2
  ERR_BAD_USERNAME = -3
  ERR_BAD_PASSWORD = -4

  def self.login(username, password)
  	user = User.find_by_user_and_password(username, password)
  	if user.blank?
  		login_data = {:errCode => ERR_BAD_CREDENTIALS}
  	else
  		user.count+=1
      user.save
  		login_data = {:errCode => SUCCESS, :count => user.count}
    end
    return login_data
  end

  def self.add(username, password)
  	user = User.find_by_user(username)
  	if username.nil? or username.blank? or username.length > 128
  		add_data = {:errCode => ERR_BAD_USERNAME}
  	elsif !user.blank?
  		add_data = {:errCode => ERR_USER_EXISTS}
  	elsif password.length > 128 
  	  add_data = {:errCode => ERR_BAD_PASSWORD}
  	else
  		User.create(:user => username, :password => password, :count => 1)
  		add_data = {:errCode => SUCCESS, :count => 1}
    end
    return add_data
  end

  def self.TESTAPI_resetFixture()
  	User.delete_all
  	reset_data = {:errCode => SUCCESS}
    return reset_data
  end
end

