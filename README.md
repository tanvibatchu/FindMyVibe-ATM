# FindMyVibe | Audio Taste Matcher
**A full-stack full-mood recommendation engine.**

## What We Made
A web application that leverages user sentiment and audio features to recommend music. 
* **Sentiment-to-Audio Mapping:** Built a custom logic layer to translate user moods into Spotify/Netflix API parameters.
* **Full-Stack Architecture:** Developed a Flask-based Python backend to handle complex API interactions and a responsive frontend for seamless user experience.
* **Stack:** Python (Flask), HTML5, JavaScript, CSS, and Shell scripting for deployment.

## Why We Made It
We wanted to explore how software can interpret subjective human emotions through objective data points. Most media recommendation engines rely on historical data (what you’ve watched); We wanted to build something that focused on the **now** (how you feel). This project was a deep dive into API integration and state management.

## What We Originally Thought
We originally thought that simply hitting an API and displaying the results would be enough. We assumed the biggest challenge would be the styling—making the "vibe" look right visually with CSS.

## 📉 What Actually Happened
* **Integration Complexity:** Handling OAuth and rate-limiting for Spotify/Netflix APIs proved significantly more complex than the UI design.
* **The "Cold Start" Problem:** If a user’s mood didn't perfectly match a genre, the results were chaotic. I had to refine the backend logic to provide "nearest neighbor" recommendations.
* **Env Management:** Managing API secrets across different environments required setting up a more robust `.env` structure than I had initially planned.

## 💡 What We Took Away
1. **API First Design:** The quality of a recommendation engine is entirely dependent on how well you handle the data source.
2. **UX is Emotional:** Users don't just want a list of songs; they want the interface to feel like the mood they selected.
3. **Python for the Web:** Using Python for a web backend taught us how to bridge the gap between data-heavy logic and real-time user interfaces.
