import React from 'react';
import { useTheme } from '@mui/material/styles';
import DashboardCard from '../../../components/shared/DashboardCard';
import Chart from 'react-apexcharts';

const SentimentSurvey = ({ tableData }) => {
  const theme = useTheme();
  const primary = theme.palette.primary.main;
  const secondary = theme.palette.secondary.main;
  const tertiary = theme.palette.error.main;

  const optionscolumnchart = {
    chart: {
      height: 350,
      type: 'line',
      dropShadow: {
        enabled: true,
        color: '#000',
        top: 18,
        left: 7,
        blur: 10,
        opacity: 0.2,
      },
    },
    colors: [primary, secondary, tertiary],
    markers: {
      size: 0.5,
    },
    stroke: {
      curve: 'smooth',
    },
    grid: {
      borderColor: '#e7e7e7',
      row: {
        colors: ['#f3f3f3', 'transparent'],
        opacity: 0.5,
      },
    },
    xaxis: {
      categories: tableData.map((i) => i['record_date']),
      type: 'datetime',
      title: {
        text: 'Day',
      },
    },
    yaxis: {
      title: {
        text: 'Percentage',
      },
      type: 'string',
      min: 0,
      max: Math.max(
        ...tableData.map((i) => (i['bearish'] ? i['bearish'] : 0)),
        ...tableData.map((i) => (i['neutral'] ? i['neutral'] : 0)),
        ...tableData.map((i) => (i['bullish'] ? i['bullish'] : 0)),
      ),
    },
    legend: {
      position: 'bottom',
    },
  };

  const seriescolumnchart = [
    {
      name: 'Bullish',
      data: tableData.map((i) => (`${i['bullish']}%` ? i['bullish'] : 0)),
    },
    {
      name: 'Neutral',
      data: tableData.map((i) => (i['neutral'] ? i['neutral'] : 0)),
    },
    {
      name: 'Bearish',
      data: tableData.map((i) => (i['bearish'] ? i['bearish'] : 0)),
    },
  ];

  return (
    <DashboardCard title="Sentiment Survey">
      <Chart options={optionscolumnchart} series={seriescolumnchart} type="line" height="270px" />
    </DashboardCard>
  );
};

export default SentimentSurvey;
