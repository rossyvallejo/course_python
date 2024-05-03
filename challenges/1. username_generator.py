print('Welcome to the username generator, this program creates a username with the exponential distribution'
      ' (pdf and CDF), the number evaluated in the pdf and CDF will be in your username!')
number = float(input('What is your favorite number between 0 and infinity?'))
n_lam = float(input('What is your favorite lambda?'))
zodiac = input('what is your zodiac sign?')
exp = 2.7182
fdp = n_lam * exp**((-1) * n_lam * number)
cdf = 1 - exp**((-1) * n_lam * number)
print(f'Your username is: {cdf}{zodiac}{fdp}')
print('Your username is: ' + str(cdf) + str(zodiac) + str(fdp))