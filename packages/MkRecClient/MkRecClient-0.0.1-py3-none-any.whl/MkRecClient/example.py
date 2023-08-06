import MkRecClient

#Register the client
usr_nm = input("My username: ")
MkRecClient.Register_Client(usr_nm)

#Get Machines
print(MkRecClient.get_machines())

#Get Machine Training Data
Machines = MkRecClient.get_machines()
print(Machines['Animals'].train_acc) #Machine accuracy
#  OR
print(Machines['Animals'].training)

#Get Machine Trained Titles, What the machines knows
Machines = MkRecClient.get_machines()
print(Machines['Animals'].titles)

#Get the value of points attached to your account
print(MkRecClient.get_points())

#Send an Image to get results!
result = MkRecClient.PredictImage(MkRecClient.prep_img("img.png"), "Animals")
result.result #the best result
result.all_results #all results
result.remaing_points #how many points you have now
result.possible_titles #all possible titles of the machine
#if the result wasn't correct, and you had heap=True
result.correct('correct class')