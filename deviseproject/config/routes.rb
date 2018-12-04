Rails.application.routes.draw do
  resources :posts
  devise_for :users

 post 'comments/create', to: 'comments#create', as: :comments
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
  root 'posts#index'
  delete 'comments/:id', to: 'comments#destroy'
  
  
  
end
