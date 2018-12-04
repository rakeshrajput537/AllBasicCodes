class CreateCountries < ActiveRecord::Migration[5.2]
  def change
    create_table :countries do |t|
      t.string :Name
      t.integer :populaton

      t.timestamps
    end
  end
end
