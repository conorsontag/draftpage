#--------------------------------
# Script to scrape information 
# from nflcombineresults.com. 

# Create a class - player. 
PersonalAtts = {"Year":0,
				"Name":0,
				"College":0,
				"POS":0
				}

Measurables = {"Height (in)":0,
			   "Weight (lbs)":0,
			   "Wonderlic":0,
			   "40 Yard":0,
			   "Bench Press":0,
			   "Vert Leap (in)":0,
			   "Broad Jump (in)":0,
			   "Shuttle":0,
			   "3Cone":0}


class Player:
	"""docstring for Player"""
	def __init__(self,PersonalAtts,Measurables):
		#super(Player, self).__init__()
		self.personal = {}
		self.measurables = {}
		for key in PersonalAtts:
			self.personal[key] = PersonalAtts[key]

		for key in Measurables:
			self.measurables[key] = Measurables[key]


# Initialize a player: 
X = Player(PersonalAtts,Measurables) 