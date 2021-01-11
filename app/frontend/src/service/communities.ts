import { GetCommunityReq, ListAdminsReq, ListCommunitiesReq, ListGroupsReq, ListMembersReq } from "../pb/communities_pb";
import client from "./client";

export async function getCommunity(communityId: number) {
  const req = new GetCommunityReq();
  req.setCommunityId(communityId)
  const response = await client.communities.getCommunity(req)
  return response.toObject()
}

/*
List sub-communities of a given community
*/
export async function listCommunities(communityId: number, pageToken?: string) {
  const req = new ListCommunitiesReq();
  req.setCommunityId(communityId)
  if (pageToken) {
    req.setPageToken(pageToken)
  }
  const response = await client.communities.listCommunities(req)
  return response.toObject()
}

export async function listGroups(communityId: number, pageToken?: string) {
  const req = new ListGroupsReq();
  req.setCommunityId(communityId)
  if (pageToken) {
    req.setPageToken(pageToken)
  }
  const response = await client.communities.listGroups(req)
  return response.toObject()
}

export async function listAdmins(communityId: number, pageToken?: string) {
  const req = new ListAdminsReq();
  req.setCommunityId(communityId)
  if (pageToken) {
    req.setPageToken(pageToken)
  }
  const response = await client.communities.listAdmins(req)
  return response.toObject()
}

export async function listMembers(communityId: number, pageToken?: string) {
  const req = new ListMembersReq();
  req.setCommunityId(communityId)
  if (pageToken) {
    req.setPageToken(pageToken)
  }
  const response = await client.communities.listMembers(req)
  return response.toObject()
}