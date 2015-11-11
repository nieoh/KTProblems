# There are m hospitals and n residents. Each hospital has a ranking of
# each resident and each resident has a ranking of each hospital in terms
# of preference.

# Return a stable matching of hospitals to residents.

# Input will be supplied as m lists of n rankings of students by
# hospitals; a list of hospital student capacities;  n lists of m
# rankings. For example suppose there are two hospitals with the
# preferences

# Hospital 0: Resident 0 > Resident 1 > Resident 2
# Hospital 1: Resident 2 > Resident 1 > Resident 0
# each hospital has capacity 1 and there are three residents with preferences
# Resident 0: Hospital 0 > Hospital 1
# Resident 1: Hospital 0 > Hospital 1
# Resident 2: Hospital 0 > Hospital 1
# then input would be stable_matching([[0,1,2], [2,1,0]], [1, 1],
# [[0,1],[0,1],[0,1]]).


# Return a stable matching formatted as a list of length m where the
# element in index k indicates which student is assigned to hospital k.
# In the above example, a valid answer would be [[0], [2]].


def stable_matching(hospital_rankings, hospital_capacities, student_rankings):
	numh = len(hospital_rankings)
	nums = len(student_rankings)
	answer = [[] for i in range(numh)]
	while sum(hospital_capacities)>0:
		h = [hospital_capacities[i]>0 for i in range(numh)].index(True)
		s = hospital_rankings[h][0]
		if s not in [item for sublist in answer for item in sublist]:
			answer[h].append(s)
			hospital_rankings[h].remove(s)
			hospital_capacities[h] = hospital_capacities[h]-1
		else:
			g =[s in answer[i] for i in range(numh)].index(True)
			if student_rankings[s].index(g) < student_rankings[s].index(h): #g is ranked higher than h
				#s stays with g
				hospital_rankings[h].remove(s)
			else: #s prefers hospital h
				#s moves to h and is removed from g's list
				answer[h].append(s)
				hospital_rankings[h].remove(s)
				hospital_capacities[h] = hospital_capacities[h]-1
				answer[g].remove(s)
				hospital_capacities[g] = hospital_capacities[g]+1
	return answer

