from selenium import webdriver

#stacey decides she wants to use firefox
browser = webdriver.Firefox()
#then she decides to go to my blog cos she wants to be cool like me (chad)
browser.get('http://127.0.0.1:8000')

#she notices that the title says blog, which is what she wants
assert 'blog' in browser.title

#she looks to see if there are submited blog posts

#then she decides to click on one to see it bigger

#she likes the post cos it made her cool

browser.quit()