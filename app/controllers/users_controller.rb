class UsersController < ApplicationController
  def login
  	@login_data = User.login(params[:user], params[:password])
  	respond_to do |format|
  		format.json {render :json => @login_data}
  	end
  end

  def add
  	@add_data = User.add(params[:user], params[:password])
  	respond_to do |format|
  		format.json {render :json => @add_data}
    end
  end
end
