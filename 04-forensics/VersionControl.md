You are able to look through git to find information about
when it was used, by who, and what for.

`git log` can be used to show every commit that has been made
to the repository, complete with the author, date, time,
comment, and the commit hash.

`git show <commit hash>` can be used to see the actual
contents of the given commit.

`git branch` can be used to view branches while `git checkout
<branch>` can be used to change branches

Using these commands you can find information about edits to
git repositories and answer questions like the following:

1. What is the email address of the employee who was
compromised?

Using `git log` we can see that the email address making
commits to this repository is gpeterson@mpd.hacknet.cityinthe.cloud

2. Each employee is assigned a flag. What is the flag that was
compromised?

There was a commit in the git log with the comment "Oops
wasn't supposed to commit that". Looking at that commit with
`git log f28a0c2e4ef9bdc2cd6e780abdbd8695485c7083` shows that
the text "SKY-LRHX-4910" was removed, which is the flag.

3. Greg thinks that he may have had additional account
credentials that were compromised. What's the name of the
service provider for that other compromised account?

On the `next` branch there is a file called `passwords.txt`.
The only thing writen inside is a Facebook password. So the
provider is Facebook.

4. What was the password on that compromised account?

The Facebook password written in `passwords.txt` is "waffles85"
