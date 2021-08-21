27 days later the code is completed its alpha and beta version, this is the first main release of bankCore!

- Report of mySQL behaviour:
    Each variable can get one value for each run. If any of variables assigned as twice or more,
    first value is erased and second one is assigned as real value. Briefly, if any of variables assigned once,
    other assignments overwrites to the same value. As an example in a single run, No: A balance has 100 tl. It 
    sends No: B balance 100 tl and it is set zero. However, No: A balance can send up to 100 tl to No: C balance 
    and No: B balance remains the same. Try to fix this issue. If each assingment is used at most once, there is 
    no problem. This circumstances is valid for all the variables that contains changeable values.
-- THE PROBLEM IS SOLVED -- 

- After 30 commits I started to work on different computer. Therefore, each commit can be as
same as the total line in code. However, the commit messages show the addition for respective
code.

- It seems it is not possible to impelement a structure that writes user's datas into
".txt" file and read/manipulate it. I stuck on reading data from ".txt" file So I jump 
the next step which is MySQL database.

- After 27th commit (12 were deleted) I release alpha version of bankCore. That is
basically the software that is ran in command prompt. It does not store any value 
of the user. I does not have currency transfer property since accounts are not saved.
Except for that issues, alpha version reflect the general purpose of bankCore application.
Properties: A user can register --> login --> deposit/withdraw money from the TRY account
or creating USD/EUR/Gold accounts. Exhange money between those balances. For now, this is
more or less bankCore implementation that is coded so far.

- After 12th commit, I connect my gitHub via different computer. I pushed it with 
force and commits are erased. Therefore, don't use force after first commit of
any code.

- With 10th commit, I split all currency methods even if they can be written in
one method with parameters. I did that since the input that user type doesn't 
return corresponding currency  value. It is better to apply currency method within
one method. Try to merge them later.