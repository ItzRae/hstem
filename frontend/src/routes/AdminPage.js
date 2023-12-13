import React from "react";
import { Box, Heading, Button } from "@chakra-ui/react";
import ProjectForm from "../components/ProjectForm"; // Import your ProjectForm component

const AdminPage = () => {
  return (
    <Box p="4">
      <ProjectForm /> {/* Include the ProjectForm component here */}
    </Box>
  );
};

export default AdminPage;