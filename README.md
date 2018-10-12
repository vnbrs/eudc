# Unnecessary Debugging Calls Exterminator, aka `udce`
Meet `udce`, a CLI tool that helps you to find and exterminatate unnecessary debugging calls on your code such as `console.log`, `byebug` and so on.

# Usage
Use it on your terminal:

```sh
$ udce . --language=ruby
  app/my_file.rb
  28. puts 'debugging session'

  spec/my_other_file.rb
  1. pry
  7. byebug

$ udce . --language=javascript
  app/main.js
  19. debugger;

  test.js
  49. console.log('duh');
```
