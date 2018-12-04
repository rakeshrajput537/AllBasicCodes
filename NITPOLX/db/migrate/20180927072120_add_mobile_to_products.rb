class AddMobileToProducts < ActiveRecord::Migration[5.2]
  def change
    add_column :products, :mobile, :integer
  end
end
