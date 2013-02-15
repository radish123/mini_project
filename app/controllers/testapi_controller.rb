class TestapiController < ApplicationController
  
  def resetFixture
  	@reset_data = User.TESTAPI_resetFixture()
  	respond_to do |format|
  		format.json {render :json => @reset_data}
  	end
  end

  def unitTests
  	`rspec > unit.txt`
  	fullOutput = File.read("unit.txt")
  	test_match = fullOutput[/(.*) examples,/, 1]
  	fail_match = fullOutput[/, (.) failure/, 1]
  	@test_data = {:totalTests => test_match.to_i, :nrFailed => fail_match.to_i, :output => fullOutput}
    #puts "@@$@$@$@$@$"
  	#puts test_match.to_i
    #puts "@@$@$@$@$@$"
  	respond_to do |format|
  		format.json {render :json => @test_data}
  	end
  end

end
