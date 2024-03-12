from main import Mlops

mlopsObj=Mlops(5)
def test_getTotalStudents():
	assert mlopsObj.getTotalStudents() == 5

def test_addStudent():
	mlopsObj.addStudent()
	assert mlopsObj.getTotalStudents() == 6

def test_removeStudent():
	mlopsObj.removeStudent()
	assert mlopsObj.getTotalStudents() == 5

def test_getClassName():
	assert mlopsObj.getClassName() == "Machine Leraning Opertaions CS-B"
