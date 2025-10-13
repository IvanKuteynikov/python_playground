def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
    
print(is_prime(788766886655576576674888076868967587508989698698986857598689589858))