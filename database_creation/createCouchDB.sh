#!/bin/bash
# create docker volume
sudo docker volume create --name couchdb

#export the variables
export declare nodes=(172.26.135.183 172.26.130.94 172.26.131.200) # put all the cluster nodes
export masternode=172.26.135.183 # put the node you are working with
export declare othernodes=`echo ${nodes[@]} | sed s/${masternode}//`   # declare nodes other than the current ones
export user='admin' # couchdb username
export pass='pass'  # couchdb password
export cookie='monkey' # cookie to connect with nodes, should be same for all the clusters
export VERSION='3.2.1' # couchdb version you want
docker pull ibmcom/couchdb3:${VERSION} # to pull couchdb docker image

# Then use the following command to create the docker container running couchdb server
sudo docker create\
      --name couchdb${masternode}\
      -v couchdb:/opt/couchdb/data\
      -p 5984:5984\
      -p 4369:4369\
      -p 9100-9300:9100-9300\
      --env COUCHDB_USER=${user}\
      --env COUCHDB_PASSWORD=${pass}\
      --env COUCHDB_SECRET=${cookie}\
      --env ERL_FLAGS="-setcookie \"${cookie}\" -name \"couchdb@${masternode}\""\
      ibmcom/couchdb3:${VERSION}

declare conts=(`docker ps --all | grep couchdb | cut -f1 -d' ' | xargs -n${size} -d'\n'`) # get container ids
for cont in "${conts[@]}"; do docker start ${cont}; done # start the containers


# To setup cluster
for node in ${othernodes} 
do
    curl -XPOST "http://${user}:${pass}@${masternode}:5984/_cluster_setup" \
      --header "Content-Type: application/json"\
      --data "{\"action\": \"enable_cluster\", \"bind_address\":\"0.0.0.0\",\
             \"username\": \"${user}\", \"password\":\"${pass}\", \"port\": \"5984\",\
             \"remote_node\": \"${node}\", \"node_count\": \"$(echo ${nodes[@]} | wc -w)\",\
             \"remote_current_user\":\"${user}\", \"remote_current_password\":\"${pass}\"}"
done

for node in ${othernodes}
do
    curl -XPOST "http://${user}:${pass}@${masternode}:5984/_cluster_setup"\
      --header "Content-Type: application/json"\
      --data "{\"action\": \"add_node\", \"host\":\"${node}\",\
             \"port\": \"5984\", \"username\": \"${user}\", \"password\":\"${pass}\"}"
done

curl -XPOST "http://${user}:${pass}@${masternode}:5984/_cluster_setup"\
    --header "Content-Type: application/json" --data "{\"action\": \"finish_cluster\"}"


# To test the connection
for node in "${nodes[@]}"; do  curl -X GET "http://${user}:${pass}@${node}:5984/_membership"; done

