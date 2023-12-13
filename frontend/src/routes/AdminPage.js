import React, { useEffect, useState } from "react";
import { useTable } from "react-table";
import axios from "axios";
import {
  Box,
  Container,
  TableContainer,
  Text,
  Table,
  Tbody,
  Tr,
  Td,
} from "@chakra-ui/react";

export default function AdminPage() {
  const [projects, setProjects] = useState([]);

  useEffect(() => {
    axios
      .get("http://localhost:8000/api/projects/")
      .then((response) => {
        setProjects(response.data);
      })
      .catch((error) => {
        console.error("Error fetching projects:", error);
      });
  }, []);

  // Commented-out columns for future use
  // const columns = React.useMemo(
  //   () => [
  //     {
  //       Header: "Project",
  //       accessor: "project", // Replace 'project' with the actual field name from your API
  //     },
  //   ],
  //   []
  // );

  return (
    <Container maxW="container.xl">
      <Box overflowX="auto">
        <TableContainer>
          <Table variant="simple">
            <Tbody>
              {projects.map((project) => (
                <Tr key={project.id}>
                  <Td>{project.title}</Td>
                  <Td>{project.description}</Td>
                </Tr>
              ))}
            </Tbody>
          </Table>
        </TableContainer>
        {/* Uncomment the following code if you want to use react-table */}
        {/* <table style={{ width: '100%', marginTop: '20px' }}>
          <thead>
            {headerGroups.map((headerGroup) => (
              <tr {...headerGroup.getHeaderGroupProps()}>
                {headerGroup.headers.map((column) => (
                  <th {...column.getHeaderProps()}>{column.render('Header')}</th>
                ))}
              </tr>
            ))}
          </thead>
          <tbody {...getTableBodyProps()}>
            {rows.map((row) => {
              prepareRow(row);
              return (
                <tr {...row.getRowProps()}>
                  {row.cells.map((cell) => {
                    return <td {...cell.getCellProps()}>{cell.render('Cell')}</td>;
                  })}
                </tr>
              );
            })}
          </tbody>
        </table> */}
      </Box>
    </Container>
  );
}