Rails.application.routes.draw do
  get 'page/index'
  get 'game/ping'
  get 'game/pong'
  get 'example/text'
  get 'credit_card/open'
  get 'credit_card/credit'
  get 'credit_card/debit'
  get 'credit_card/close'
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
