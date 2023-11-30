FROM ubuntu:latest

WORKDIR /app

RUN apt-get update && apt-get upgrade -y

RUN apt-get install maven git openjdk-11-jre wget vim -y

RUN wget https://get.jenkins.io/war-stable/2.387.2/jenkins.war

ENTRYPOINT ["java", "-jar", "jenkins.war", "-Djava.awt.headless=true"]
