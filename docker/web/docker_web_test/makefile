image = "icl/docker-web-test"
container = "Web_test_container"
user="web_test_user"
localpath="/home/icl/docker-storage/Web/test"
#path= ${localpath}":/home/"${user}
path= ${localpath}:"/data"

image:
	docker build -t ${image} --network my-net .
run:
	docker run -dt --network my-net --name ${container} -v${path} ${image}
exec:
	docker exec -it ${container} bash
clean:
	docker stop ${container}
	docker rm ${container}

cleani:
	docker rmi ${image}
