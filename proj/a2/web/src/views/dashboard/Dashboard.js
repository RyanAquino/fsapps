import React, { useEffect, useState } from 'react';
import { Grid, Box } from '@mui/material';
import PageContainer from 'src/components/container/PageContainer';

// components
import DTSTables from './components/DTSTables';
import YearlyBreakup from './components/YearlyBreakup';
import RecentTransactions from './components/RecentTransactions';
import ProductPerformance from './components/ProductPerformance';
import Blog from './components/Blog';
import MonthlyEarnings from './components/MonthlyEarnings';
import SentimentSurvey from './components/SentimentSurvey';
import { useNavigate } from 'react-router-dom';
import { fetchDTSTables, fetchSentimentSurvey } from '../../api/utils';

const Dashboard = () => {
  const loginRoute = '/auth/login';
  const navigate = useNavigate();
  const [dtsTableData, setDTSTableData] = useState([]);
  const [sentimentData, setSentimentData] = useState([]);

  useEffect(() => {
    const token = localStorage.getItem('token');
    if (!token) {
      navigate(loginRoute);
    }

    Promise.all([
      fetchDTSTables('deposits_withdrawals_operating_cash_balance'),
      fetchSentimentSurvey(),
    ])
      .then((data) => {
        let [dtsData, sentiment] = data;
        let dtsDataFormatted = [];
        let dates = [];

        for (const item of dtsData) {
          if (dates.includes(item['record_date'])) {
            continue;
          }
          dates.push(item['record_date']);
          dtsDataFormatted.push({
            deposits: item['transaction_today_amt_deposits'],
            withdrawals: item['transaction_today_amt_withdrawals'],
            total: item['total_transaction_today'],
            date: item['record_date'],
          });
        }

        let sentimentDataFormatted = [];

        for (const item of sentiment) {
          sentimentDataFormatted.push({
            record_date: item['record_date'],
            bullish: item['bullish'],
            neutral: item['neutral'],
            bearish: item['bearish'],
          });
        }

        setSentimentData(sentimentDataFormatted);
        setDTSTableData(dtsDataFormatted);
      })
      .catch((err) => {
        if (err.response.status === 401) {
          navigate(loginRoute);
        }
      });
  }, []);

  return (
    <PageContainer title="Dashboard" description="this is Dashboard">
      <Box>
        <Grid container spacing={3}>
          <Grid item xs={12} lg={12}>
            <DTSTables tableData={dtsTableData} />
          </Grid>
          <Grid item xs={12} lg={12}>
            <SentimentSurvey tableData={sentimentData} />
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
