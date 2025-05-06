# 📘 Reflection

---

## **📊 How We Selected Our Datasets**

To select the datasets for this weather chatbot project, we focused on finding reliable, structured sources that would support both historical and real-time weather data needs. For the static dataset, we found a CSV file from Kaggle that includes capital city names along with corresponding average temperature in Celsius and UV index values. This dataset was ideal because it provided consistent, easily accessible baseline weather indicators for a global set of cities. This also formed the foundation for the chatbot’s contextual responses for the bonus section. For dynamic weather data, we used the Open-Meteo API, which offers real-time weather metrics such as wind speed and supports flexible location-based queries using latitude and longitude. The combination of these two sources—one static and one real-time—enabled us to create a chatbot that can provide meaningful and up-to-date answers. Our selection process focused mainly on data quality because we wanted to cover a full range of information that was up to date for our project. We also used datasets that were simple to integrate based on our class assignments and walkthroughs.

---

## **⚠️ Challenges or Problems Faced During the Process**

One of the main challenges during the development of this weather chatbot was using multiple data sources. The ETL process posed some difficulties at first, especially when having to normalize city names between the static CSV dataset and the real-time API. Inconsistencies in spelling, casing, or regional naming conventions caused mismatches in query results. We needed to make sure our data was clean and avoided duplicates, which required careful transformations. Another significant hurdle was handling API limitations and error responses from the Open-Meteo service. Sometimes, data was unavailable for certain locations, or the API returned unexpected formats, which needed custom error handling.

Deploying the Flask app on a Google Cloud VM introduced its own set of issues, including configuring firewall rules, managing dependencies in a virtual environment, and ensuring that the app remained accessible publicly without downtime. Also, with the Discord bot, we ran into some troubles with bot tokens, ensuring accurate message parsing, and keeping the logic consistent between platforms to make sure our Discord bot behaved like its Flask counterpart while remaining responsive and error-tolerant.

Lastly, working as a group was only a little challenging. Sometimes, coordinating who was handling what slowed down our project time, and we occasionally ran into overlap by working on the same code. Clear communication and dividing tasks helped us overcome this and keep the project on track. Despite these challenges, we were able to learn a lot and ensure our project ran smoothly.

---

## **🧠 Key Learnings and Discoveries**

Throughout the development of this project, we gained a better understanding of how to integrate and manage both static and dynamic data sources within a real-world application. One major learning was the importance of data cleaning, which had a huge impact when matching user inputs to dataset entries—especially when dealing with global city names and inconsistent formatting. We also discovered how manageable Flask can be for rapidly building web APIs, as it worked quite well for our needs.

Working with the Open-Meteo API taught us how to handle asynchronous external requests and the importance of planning for missing or incomplete data responses. We also learned more about setting up and maintaining a Google Cloud VM, which gave us experience in cloud computing, server configuration, and hosting in real-world environments. 

Lastly, incorporating Discord integration introduced us to event-driven programming using `discord.py`. This showed us how chatbot logic can be extended across platforms. It also sparked interest in creating other types of Discord bots, whether useful or just for fun in friends' servers!

Collaborating as a team on the coding side taught us how to navigate version control in GitHub, divide tasks effectively, and review each other's code to maintain consistency and avoid conflicts. Overall, this project strengthened our skills in working with external data, web development, deployment, and team-based problem-solving.

---

## **🚀 What Enhancements or Features Would You Have Added with More Time?**

There are several features we would have liked to implement if we had more time to expand the project. Some of them would be complex to complete independently, but they would significantly enhance the functionality and user experience. 

First, we would have added support for multiple languages, allowing the chatbot to respond to weather questions in users' native tongues—or even in regional slang—making it more globally accessible. We also considered integrating more detailed weather data from the API, such as precipitation, humidity, and forecast trends, and even storing historical weather data so users could compare conditions over time.

On the interface side, we envisioned adding interactive maps or dropdown city selectors to reduce user input errors and make the app look more polished and professional. For the Discord bot, implementing rich embeds with weather icons, graphs, and color-coded alerts would greatly enhance user engagement.

Lastly, we would have explored creating user accounts with saved preferences and chat history, to make the experience more personalized and efficient for regular users. With additional time, these enhancements could evolve the project into a fully production-ready tool—and potentially even a mobile app available to the public.