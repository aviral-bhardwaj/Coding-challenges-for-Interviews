def budgetShopping(n, bundleQuantities, bundleCosts):
    
    if not bundleQuantities or not n:
        return 0
    index = [bundleCosts.index(x) for x in sorted(bundleCosts)]
    bundleCosts = [bundleCosts[i] for i in index]
    bundleQuantities = [bundleQuantities[i] for i in index]
    
    if n < bundleCosts[0]:
      return 0
    countQuant = [0] * (n + 1)
    
    for i in range(bundleCosts[0], n + 1):
      j = 0
      while (j < len(bundleCosts)):
          if i < bundleCosts[j]:
              break
          temp = countQuant[i - bundleCosts[j]] + bundleQuantities[j]
          countQuant[i] = max(temp, countQuant[i])
          j = j + 1
    return countQuant[n]
    
print (budgetShopping(50, [20, 19], [24, 20]))