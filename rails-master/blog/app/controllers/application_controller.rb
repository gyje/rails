class ApplicationController < ActionController::Base
  protect_from_forgery with: :exception
  def hello
      render html: "hello,rails,thanks coding webide,中文测试"
  end
  def goodbay
      render html: "goodbay"
  end
end
