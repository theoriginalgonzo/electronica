The Never Winter Bank website has a code vulnerability in its
JavaScript, and none of the questions are about that dispite
the exploitation of that vulnerability being the whole point.
So I am going to tell you what that is now.

``` js
if (parseInt(amount) < account.amount) {
  if ((account.amount - parseInt(amount)) < account.minimum) {
    return res.status(400).send('Error: Account is not allowed to have a balance lower than 10');
  }
  var transferAmount = parseInt(amount, 10);
  account.amount -= transferAmount;

}
```

Basically that third call of `parseInt` (`parseInt(amount, 10)`)
has a second input, called a radix, and that radix is set to 10.
This means that during that string (`amount`) will be treated
as a decimal number, where in the first two calls no radix is
specified. When no radix is specified the `parseInt` function
will treat any string entered that starts with a will be
treated as an octal. So given `amount` = 01000, the first two
calls will return `512` but the third will return `1000`. So
by using `01000` as an input string the code will check if the
account has $512 for the transaction and if removing $512 will
leave the account with less than $10, but at the final call it
calculates the ammount to transfer as a decimal giving back
$1000.

1. What is the path of the leaked file?

Find a way to access the site's `robots.txt` file, that will
contain the path.

2. What is the flag?

Enter a value in octal between the decimal values of 512 and
990.
