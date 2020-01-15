Collin Bauer

CSCI 392 - Ethics in Computing

---

## Answers to Software Engineering Ethics Parts 1-3


### Q 1.1
#### What kinds of harm has Mike probably suffered as a result of this incident? What kinds of harm has Sarah probably suffered? (Make your answers as full as possible; identify as many kinds of harm done as you can think of).

    Ouch. Mike had plenty of funds saved for his daughter to attend the college, but thanks to the failure of the software, slow bureaucratic processes of the bank, and inflexibility of the college, both Mike and Sarah suffered much unneccesary harm.

    - Mike has likely experinced anger at both the bank and the college, and sorrow towards his daughter, thus has suffered emotional harm.
    - Sarah has also experienced emotional harm, and may feel disappointed at her father or angry at the general situation
    - The software glitch itself is a form of financial harm. It may have caused financial instability for Mike and his family, due to funds being unavailable for a period of time.
    - This also presents harm to Sarah's future, as her father was forced to tell her that she is not attending college next fall.

<br/>

### Q 1.2
#### Could the problem with Mike’s account have been the result of an action (or a failure to perform an action) by a software engineer? How many possible scenarios/explanations for this event can you think of that involve the conduct of one or more software engineers? Briefly explain the scenarios:

    There is a lot to consider when engineering new software, and many risks associated with various projects. Banking and financial software are especially sensitive, as an unforseen bug may cause harm to many peoples and institutes.

    Perhaps this withdrawal hit an edge case not thoroughly tested - a value that either overflows, underflows, or that is not rounded correctly. This would have been an oversight on the software tester's part.

    It could have also been user error, with a bank teller inputting a wrong number that was not handled by the software porperly. This should also be accounted for in software testing, where possible.

    Maybe there was a backdoor in the software, and a bad actor, either inside the bank, or the college, or a third party, was able to intercept the transaction and reroute it to themselves. Maybe this backdoor was put there by the engineers, so they may abuse the banking system themselves.

    There is also the possibility of the transaction being lost in transit, caused by an outage, bad security credentials, or network packet loss. This is a very difficult problem to solve, but some receipt system could be in place to help mitigate these risks.

<br/>

### Q 1.3
#### Taking into account what we said about ethics in the introduction, could any of the scenarios you imagined involve an ethical failure of the engineer(s) responsible? How? Explain:

**Note: An ethical failure would be preventable, and one that a good human being with appropriate professional care and concern would and should have prevented (or at least have made a serious effort to prevent).*

    Edge cases and user error may be preventable, but absent mindedness is not a failure of ethics, but of knowledge. Of the above scenarios, the biggest ethical failure would be the introduction of a backdoor to the software. Serious measures should be made to deny such a bug or "feature" to exist. Various checking mechanisms should also be designed to detect and prevent a backdoor attempt. Bank workers trained in the software should understand what to do ethically if they ever discover such a bug in the software.

<br/>

### Q 1.4
#### In what ways could Karen potentially be harmed by this app, depending on how it is designed and how her shopping data is handled and used? Identify a few harmful scenarios you can think of, and the types of harm she could suffer in each:

    I wouldn't be surprised if this app already exists. (Heck, it may as well be Google Maps.) Many common mobile apps use these very practices of collecting personal data and selling it for profit. They usually claim this data is "anonymous", but end-users have no way of knowing if this is true.

    For Karen's part, this app represents a risk on her privacy. Since this data is on a serever, if it is not anonymized, someone could hack into it and steal her information, including her financial information, and possibly identity.
    
    Someone with malintent could use this information to track her movements and predict where she is going next. This could be a stalker or someone who wishes her harm, or even death. This scenario is unlikely, but definitely a scary one.

<br/>

### Q 1.5
#### Which if any of these harms could result from ethical failings on the part of the people who developed Errand Whiz? How, specifically?

    If the developers plan on using the data they collect from Karen and other customers to sell to other companies, perhaps there are other customers than just Facebook buying it. There is a large black market for information which may be stolen and exploited for financial gain, among other things. Selling this data to such a customer would be a large ethical failure.

<br/>

### Q 1.6
####  What actions could the people behind Errand Whiz take to prevent these harms? Are they ethically obligated to prevent them? Why or why not? Explain your answer.

    Many app developers work design their part of the app, then move on once it is finished. The app is bought by a larger company, and they maintain it in the long term. Since this data is collected long term, many questions on how to use it fall on them. The original Errand Whiz devs might have designed the app with good intent, but have no control over how the operating company handles this information.
    
    An ethical company would keep this information as anonymous as possible and inform users just how much information is collected and how it is used. This is typically explained in the terms of use agreement but important parts should be highlighted somewhere in the UI. It could even have an opt-out system for users who do not want their data collected, or even a way to have personal data already collected removed from their database.

    Of course, one could argue that the app could have been designed to not collect personal data at all, but in the current mobile landscape, this would not have been a very marketable decision.