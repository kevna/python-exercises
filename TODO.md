ackermann
---------
- [ ] make the caching more generic by moving from a 2D dict `cache[m][n]=a` to an args tuple `cache[(m,n)]=a`
- [ ] consider if caching can be done as a decorator rather than integrating it into the function
- [ ] consider if we should move `cache.__str__` to `cache.__repr__` since it's not intended for public consumption
