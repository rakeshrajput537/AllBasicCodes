Rails.application.routes.draw do
  get 'sessions/new'
  get 'teachers/new'
  
  get 'welcome/index'

  get "log_out" => "sessions#destroy", :as => "log_out"
  get "log_in" => "sessions#new", :as => "log_in"
  get "sign_up" => "teachers#new", :as => "sign_up"
  root :to => "teachers#new"
  resources :teachers
  resources :sessions



  resources :articles do 
  	resources :comments
  end
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
