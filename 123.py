class Device():
  def __init__(self):
    self.__typeD = ''
    self.__memory = ''
    self.__year = 0
  def set_type(self,typeD):
    self.__typeD = typeD;
  def get_type(self):
    return self.__typeD
  def set_memory(self,memory):
    self.__memory = memory;
  def get_memory(self):
    return self.__memory
  def set_year(self,year):
    self.__year = year;
  def get_year(self):
    return self.__year
  def info(self):
    print(f'Тип устройства: {self.__typeD} \nПамять: {self.__memory} \nГод выпуска: {self.__year}')

class Phone(Device):
  def __init__(self):
    super().__init__()
    self.__brand = ''
    self.__model = ''
  def set_brand(self, brand):
    self.__brand = brand
  def get_brand(self):
    return self.__brand
  def set_model(self, model):
    self.__model = model
  def get_model(self):
    return self.__model
  def info(self):
    super().info()
    print(f'Марка: {self.__brand} \nМодель: {self.__model}')

Ph = Phone()
Ph.set_type('Phone')
Ph.set_brand('Samsung')
Ph.set_model('Galaxy a32')
Ph.set_memory('128 Гб')
Ph.set_year(2018)

print(Ph.get_model())
Ph.info()