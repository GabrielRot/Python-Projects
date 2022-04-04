#!/usr/bin/env python
# coding: utf-8

# In[1]:


from hashlib import sha256


# In[2]:


text='ABC'


# In[3]:


print(sha256(text.encode('ascii')).hexdigest())


# In[9]:


from hashlib import sha256
def SHA256(text):
    return sha256("ABC".encode("ascii")).hexdigest()
def mine(block_number,transactions,previous_hash,prefix_zeros):
    nonce=1
    text=str(block_number)+transactions+previous_hash+str(nonce)
    new_hash=SHA256(text)
    return new_hash
if __name__=='__main__':
    transactions= '''
    abir->nabil->20,
    sajid->labib->15,
    '''
    new_hash=mine(5,transactions,'b5d4045c3f466fa91fe2cc6abe79232a1a57cdf104f7a26e716e0a1e2789df78',4)
    print(new_hash)


# In[15]:


from hashlib import sha256
max_nonce=10000000
def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()
def mine(block_number,transactions,previous_hash,prefix_zeros):
    prefix_str='0'*prefix_zeros
    for nonce in range(max_nonce):
        text=str(block_number)+transactions+previous_hash+str(nonce)
        new_hash=SHA256(text)
        if new_hash.startswith(prefix_str):
            print(f"yay! you have mined bitcoin with the value of :{nonce}")
            return new_hash
    return new_hash
    raise BaseException("could not find the correct after trying {max_nonce}times")
if __name__=='__main__':
    transactions= '''
    abir->nabil->20,
    sajid->labib->15,
    '''
    difficulty=4
    import time
    start= time.time()
    print("start mining")
    new_hash=mine(5,transactions,'b5d4045c3f466fa91fe2cc6abe79232a1a57cdf104f7a26e716e0a1e2789df78',difficulty)
    total_time=str((time.time()-start))
    print(f"end mining.Mining took:{total_time}seconds")
    print(new_hash)


# In[ ]: