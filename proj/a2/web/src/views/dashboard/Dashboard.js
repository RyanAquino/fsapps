import React from 'react';
import { Grid, Box } from '@mui/material';
import PageContainer from 'src/components/container/PageContainer';

// components
import DTSTables from './components/DTSTables';
import YearlyBreakup from './components/YearlyBreakup';
import RecentTransactions from './components/RecentTransactions';
import ProductPerformance from './components/ProductPerformance';
import Blog from './components/Blog';
import MonthlyEarnings from './components/MonthlyEarnings';
import SentimentSurvey from "./components/SentimentSurvey";

const Dashboard = () => {
  return (
    <PageContainer title="Dashboard" description="this is Dashboard">
      <Box>
        <Grid container spacing={3}>
          <Grid item xs={12} lg={12}>
            <DTSTables />
          </Grid>
            <Grid item xs={12} lg={12}>
                <SentimentSurvey />
            </Grid>
          {/*<Grid item xs={12} lg={4}>*/}
          {/*  <Grid container spacing={3}>*/}
          {/*    <Grid item xs={12}>*/}
          {/*      <YearlyBreakup />*/}
          {/*    </Grid>*/}
          {/*    <Grid item xs={12}>*/}
          {/*      <MonthlyEarnings />*/}
          {/*    </Grid>*/}
          {/*  </Grid>*/}
          {/*</Grid>*/}
          {/*<Grid item xs={12} lg={4}>*/}
          {/*  <RecentTransactions />*/}
          {/*</Grid>*/}
          {/*<Grid item xs={12} lg={8}>*/}
          {/*  <ProductPerformance />*/}
          {/*</Grid>*/}
          {/*<Grid item xs={12}>*/}
          {/*  <Blog />*/}
          {/*</Grid>*/}
        </Grid>
      </Box>
    </PageContainer>
  );
};

export default Dashboard;
