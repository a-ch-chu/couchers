import { Box, Card, CardContent, IconButton } from "@material-ui/core";
import { makeStyles } from "@material-ui/core/styles";
import ExpandLessIcon from "@material-ui/icons/ExpandLess";
import ExpandMoreIcon from "@material-ui/icons/ExpandMore";
import React, { useState } from "react";
import Avatar from "../../../components/Avatar";
import { HostRequest } from "../../../pb/requests_pb";
import { formatDate, timestamp2Date } from "../../../utils/date";
import { useUser } from "../../userQueries/useUsers";
import TimeInterval from "../messagelist/MomentIndication";
import UserName from "../messagelist/UserName";

const useStyles = makeStyles({
  root: { display: "flex" },
  card: { flexGrow: 1 },
  name: { flexGrow: 1 },
});

export interface HostRequestListItemProps {
  hostRequest: HostRequest.AsObject;
}

export default function HostRequestListItem({
  hostRequest,
}: HostRequestListItemProps) {
  const [expanded, setExpanded] = useState<boolean>(false);
  const classes = useStyles();
  const { data: otherUser } = useUser(hostRequest.fromUserId);
  return (
    <>
      <Card className={classes.root}>
        {otherUser && <Avatar user={otherUser} />}
        <Box className={classes.card}>
          <Box className={classes.root}>
            {otherUser && (
              <UserName user={otherUser} className={classes.name} />
            )}
            <TimeInterval date={timestamp2Date(hostRequest.created!)} />
            <IconButton
              onClick={(event) => {
                event.stopPropagation();
                setExpanded(!expanded);
              }}
            >
              {expanded ? <ExpandLessIcon /> : <ExpandMoreIcon />}
            </IconButton>
          </Box>
          <CardContent style={{ maxHeight: expanded ? "unset" : "4em" }}>
            {hostRequest.latestMessage?.text?.text || ""}
          </CardContent>
        </Box>
      </Card>
      <Box>
        You requested to Surf:{formatDate(hostRequest.fromDate)}
        {" - "}
        {formatDate(hostRequest.toDate)}
      </Box>
    </>
  );
}
