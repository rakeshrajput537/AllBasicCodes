class Item < ApplicationRecord
  belongs_to :category, touch:true
end
