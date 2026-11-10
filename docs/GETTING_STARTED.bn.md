# CreativeCode Engine — বাংলায় ব্যবহার

CreativeCode Engine v0.1.0 একটি **AI Design Workflow Toolkit**। এটি স্বয়ংক্রিয়ভাবে ওয়েবসাইট বানায় না। কোনো নতুন AI Model, API Key বা Server দরকার নেই। আপনার ব্যবহার করা AI Assistant-কে Rules ও Prompts দিতে হবে।

## শুরু করার নিয়ম

1. GitHub থেকে Repository Download করুন অথবা `git clone` করুন।
2. `01_DESIGN_RULEBOOK.md`, `02_CREATIVE_WORKFLOW.md` ও `prompts/creative_director.md` AI-কে দিন।
3. `examples/sample_brief.md` দেখে নিজের প্রজেক্টের প্রয়োজন, ব্যবহারকারী, অনুমোদিত ডিজাইন এবং সীমাবদ্ধতা লিখুন।
4. AI-কে **তিনটি সত্যিকারের আলাদা Layout ও Interaction Concept** তৈরি করতে বলুন; শুধু রং পরিবর্তন গ্রহণ করবেন না।
5. `prompts/design_critic.md` ও `03_REVIEW_SCORECARD.md` দিয়ে Concept Review করুন।
6. একটি Concept পছন্দ করার পরেই `prompts/implementation_engineer.md` ব্যবহার করে কোড তৈরি করুন।
7. Live Site-এ দেওয়ার আগে আলাদা পরিবেশে Mobile/Desktop, Security ও Functional Test করুন।

## Python Score Calculator

Python 3.10+ থাকলে:

```sh
python3 tools/score.py examples/sample_review.json
python3 -m unittest discover -s tools -p 'test_*.py' -v
```

এটি **রিভিউয়ের নম্বর হিসাব করে**। নিজে ডিজাইন দেখে যাচাই করে না। কোনো Test না হলে `not_tested` লিখুন। `UNVERIFIED` মানে যাচাই অসম্পূর্ণ।

**সীমাবদ্ধতা:** এখানে AI Model, Browser Automation, Automatic Website Builder বা Hosting নেই। আপনার AI Assistant-এর Service খরচ আলাদা হতে পারে।
