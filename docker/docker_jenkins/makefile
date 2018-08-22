
image = "icl/docker-jenkins"
container = "Jenkins"
#path= "/home/icl/docker-storage:/daata"
#path="Storage"
path= "/home/icl/docker-storage/jenkins/"
#path= "~/docker-storage/jenkins/"

image:
	docker build -t ${image} --network my-net .
run:
	#docker run -dt --network my-net --name ${container}  -v ${path} ${image}
	mkdir -p ${path}
	docker run -dt -p 8080:8080 -p 50000:50000 --network my-net --name ${container} -v ${path}:/var/jenkins_home ${image}
exec:
	docker exec -it ${container} bash
stop:
	docker stop ${container}
start:
	docker start ${container}
clean:
	docker stop ${container}
	docker rm ${container}
cleani:
	docker rmi ${image}

