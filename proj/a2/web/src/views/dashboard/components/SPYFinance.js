import React, { useEffect, useState } from 'react';
import { Select, MenuItem } from '@mui/material';
import { useTheme } from '@mui/material/styles';
import DashboardCard from '../../../components/shared/DashboardCard';
import Chart from 'react-apexcharts';
import { fetchDTSTables, fetchSPYFinance } from '../../../api/utils';
import { useNavigate } from 'react-router-dom';
import dayjs from 'dayjs';

const SPYFinance = () => {
  const [data, setData] = useState([]);
  const loginRoute = '/auth/login';
  const navigate = useNavigate();

  useEffect(() => {
    const fetchDashboardData = async () => {
      const spyFinanceData = await fetchSPYFinance();
      let formattedData = [];

      for (const item of spyFinanceData.splice(-365)) {
        formattedData.push({
          x: `${new Date(item["record_date"]).toDateString()} UTC`,
          y: [item['open'], item['high'], item['low'], item['close']],
        });
      }
      setData(formattedData);
    };
    fetchDashboardData().catch((err) => {
      if (err.response.status === 401) {
        localStorage.removeItem('token');
        navigate(loginRoute);
      }
    });
  }, []);

  // chart color
  const theme = useTheme();
  const primary = theme.palette.primary.main;
  const secondary = theme.palette.secondary.main;
  const tertiary = theme.palette.error.main;

  // chart
  const optionscolumnchart = {
    chart: {
      type: 'candlestick',
      height: 350,
      zoom: {
        autoScaleYaxis: true,
      },
    },
    xaxis: {
      type: 'category',
      labels: {
        formatter: function (value) {
          return dayjs(value).format('MMM DD');
        },
      },
    },
    yaxis: {
      tooltip: {
        enabled: true,
      },
    },
  };

  const seriescolumnchart = [
    {
      data: data,
    },
  ];

  return (
    <DashboardCard title="SPDR S&P 500 ETF Trust (SPY)">
      <Chart
        options={optionscolumnchart}
        series={seriescolumnchart}
        type="candlestick"
        height="270px"
      />
    </DashboardCard>
  );
};

export default SPYFinance;
