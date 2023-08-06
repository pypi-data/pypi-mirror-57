class Submarine:

	'''
		---------------------
		Test Documentation

		นี่คือโปรแกรมสำหรับเรือดำน้ำ
		---------------------
	'''


	def __init__(self,price=15000,budget=100000):
	
		self.captain = 'Prawit'
		self.sub_name = 'Uncle I'
		self.price = price #Million
		self.kilo = 0
		self.budget = budget
		self.totalcost = 0

	def Missile(self):
		print('We are Department of Missile')

	def CalCommission(self):
		'''นี่คือฟังชันว่าลุงวิศวกร ได้คอมมิสชั่นกี่บาท'''
		pc = 10 #10%
		percent = self.price * (10/100)
		print('Long! You got: {} Million Baht'.format(percent))

	def Goto(self,enemypoint,distance):
		print(f"Let's go to {enemypoint}  Distance: {distance} KM")
		self.kilo = self.kilo + distance
		self.Fuel()
		#self.kilo += distance

	def Fuel(self):
		deisel = 20 #20 Baht/litre
		cal_fuel_cost = self.kilo * deisel
		print('Current Fuel Cost: {:,d}Baht'.format(cal_fuel_cost))
		self.totalcost += cal_fuel_cost

	@property
	def Budgetremaining(self):
		remaining = self.budget - self.totalcost
		print('Budgetremaining: {:,.2f} Baht'.format(remaining))
		return remaining



class ElectricSubmarine(Submarine):

	def __init__(self,price,budget):
		self.sub_name = 'Uncle III'
		self.battery_distance = 100000
		# Submarine can go out 100000 km/100 percent
		super().__init__(price,budget)

	def Battery(self):
		allbattery = 100
		print('KILO',self.kilo)
		calculate = (self.kilo / self.battery_distance) * 100
		print('CAL:' ,calculate)
		print("We have Battery: {}%".format(allbattery-calculate))

	def Fuel(self):
		kilowatcost = 20 #20 Baht/litre
		cal_fuel_cost = self.kilo * kilowatcost
		print('Current Power Cost: {:,d}Baht'.format(cal_fuel_cost))
		self.totalcost += cal_fuel_cost


if __name__ == '__main__':

	tesla = ElectricSubmarine(40000,2000000)
	print(tesla.captain)
	print(tesla.budget)
	tesla.Goto('Japan',10000)
	print(tesla.Budgetremaining)
	tesla.Battery()

	print('----------------')

	Kongtabbok = Submarine(40000,2000000)
	print(tesla.captain)
	print(tesla.budget)
	tesla.Goto('Japan',10000)
	print(tesla.Budgetremaining)
	

'''
kongtabreuw = Submarine(64365) #กองทัพเรือ
print(kongtabreuw.captain)
print(kongtabreuw.sub_name)
print('-------------')
print(kongtabreuw.kilo)
kongtabreuw.Goto('China',7000)
print(kongtabreuw.kilo)
kongtabreuw.Fuel()
current_budget = kongtabreuw.Budgetremaining
print(current_budget * 0.2)

kongtabreuw.CalCommission()
#####################################
print('-----Sub No.2------')
kongtabbok = Submarine(70000)
print('Before...')
print(kongtabbok.captain)
print('After...')
kongtabbok.captain = 'Srivara'
print(kongtabbok.captain)
'''
